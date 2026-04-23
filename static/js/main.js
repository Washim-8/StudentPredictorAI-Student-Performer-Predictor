/**
 * main.js — Student Performer Predictor
 * Handles: form validation, sliders, mobile nav, animations
 */

/* ── Mobile Nav Toggle ─────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('nav-toggle');
    const navLinks = document.getElementById('nav-links');

    if (toggle && navLinks) {
        toggle.addEventListener('click', () => {
            const isOpen = navLinks.classList.toggle('open');
            toggle.setAttribute('aria-expanded', isOpen);
            // Animate hamburger
            toggle.classList.toggle('active');
        });

        // Close nav on outside click
        document.addEventListener('click', (e) => {
            if (!toggle.contains(e.target) && !navLinks.contains(e.target)) {
                navLinks.classList.remove('open');
                toggle.setAttribute('aria-expanded', 'false');
                toggle.classList.remove('active');
            }
        });
    }
});

/* ── Slider Sync ───────────────────────────────────────────── */
function syncSlider(fieldId, value, suffix = '') {
    const input = document.getElementById(fieldId);
    const badge = document.getElementById(`${fieldId}-badge`);
    const slider = document.getElementById(`${fieldId}-slider`);

    if (input) input.value = value;
    if (badge) badge.textContent = parseFloat(value).toFixed(fieldId === 'assignments_completed' ? 0 : 1) + suffix;

    // Update slider fill color
    if (slider) {
        const min = parseFloat(slider.min);
        const max = parseFloat(slider.max);
        const pct = ((value - min) / (max - min)) * 100;
        slider.style.background = `linear-gradient(to right, var(--c-primary), var(--c-primary)) 0 / ${pct}% 100% no-repeat rgba(0,0,0,0.06)`;
    }

    // Trigger validation
    if (input) validateField(input);
}

// Sync input → slider
document.addEventListener('DOMContentLoaded', () => {
    const fieldIds = ['attendance', 'internal_marks', 'study_hours_per_day', 'previous_cgpa', 'assignments_completed'];
    fieldIds.forEach(id => {
        const input = document.getElementById(id);
        const slider = document.getElementById(`${id}-slider`);
        if (input && slider) {
            input.addEventListener('input', () => {
                slider.value = input.value;
                const suffix = id === 'study_hours_per_day' ? 'h' : '';
                const badge = document.getElementById(`${id}-badge`);
                if (badge) badge.textContent = parseFloat(input.value || 0).toFixed(id === 'assignments_completed' ? 0 : 1) + suffix;
                const min = parseFloat(slider.min);
                const max = parseFloat(slider.max);
                const pct = ((input.value - min) / (max - min)) * 100;
                slider.style.background = `linear-gradient(to right, var(--c-primary), var(--c-primary)) 0 / ${pct}% 100% no-repeat rgba(0,0,0,0.06)`;
            });
        }
    });
});

/* ── Extracurricular Toggle ─────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
    const radios = document.querySelectorAll('input[name="extracurricular"]');
    radios.forEach(radio => {
        radio.addEventListener('change', () => {
            document.querySelectorAll('.toggle-option').forEach(opt => opt.classList.remove('active'));
            radio.closest('.toggle-option').classList.add('active');
        });
    });
});

/* ── Real-Time Validation ───────────────────────────────────── */
const VALIDATION_RULES = {
    attendance:            { min: 0, max: 100, label: 'Attendance' },
    internal_marks:        { min: 0, max: 100, label: 'Internal Marks' },
    study_hours_per_day:   { min: 0, max: 10,  label: 'Study Hours' },
    previous_cgpa:         { min: 0, max: 10,  label: 'Previous CGPA' },
    assignments_completed: { min: 0, max: 10,  label: 'Assignments Completed' },
};

function validateField(input) {
    const id = input.id;
    const rule = VALIDATION_RULES[id];
    if (!rule) return true;

    const errorEl = document.getElementById(`${id}-error`);
    const val = parseFloat(input.value);

    input.classList.remove('error', 'valid');
    if (errorEl) errorEl.textContent = '';

    if (input.value.trim() === '' || isNaN(val)) {
        input.classList.add('error');
        if (errorEl) errorEl.textContent = `${rule.label} is required.`;
        return false;
    }

    if (val < rule.min || val > rule.max) {
        input.classList.add('error');
        if (errorEl) errorEl.textContent = `${rule.label} must be between ${rule.min} and ${rule.max}.`;
        return false;
    }

    input.classList.add('valid');
    return true;
}

document.addEventListener('DOMContentLoaded', () => {
    Object.keys(VALIDATION_RULES).forEach(id => {
        const input = document.getElementById(id);
        if (input) {
            input.addEventListener('blur', () => validateField(input));
            input.addEventListener('input', () => {
                if (input.classList.contains('error')) validateField(input);
            });
        }
    });
});

/* ── Form Submit Validation + Loading ───────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const btn = document.getElementById('predict-btn');

    if (form && btn) {
        form.addEventListener('submit', (e) => {
            let valid = true;
            Object.keys(VALIDATION_RULES).forEach(id => {
                const input = document.getElementById(id);
                if (input && !validateField(input)) valid = false;
            });

            if (!valid) {
                e.preventDefault();
                // Scroll to first error
                const firstError = form.querySelector('.form-input.error');
                if (firstError) firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
                return;
            }

            // Show loading state
            btn.classList.add('loading');
            btn.disabled = true;
        });
    }
});

/* ── Reset Form ─────────────────────────────────────────────── */
function resetForm() {
    // Clear validation styles
    document.querySelectorAll('.form-input').forEach(el => {
        el.classList.remove('error', 'valid');
    });
    document.querySelectorAll('.form-error').forEach(el => {
        el.textContent = '';
    });

    // Reset sliders to defaults
    const defaults = {
        'attendance': { val: 75, suffix: '' },
        'internal_marks': { val: 70, suffix: '' },
        'study_hours_per_day': { val: 5, suffix: 'h' },
        'previous_cgpa': { val: 7.5, suffix: '' },
        'assignments_completed': { val: 7, suffix: '' },
    };
    Object.entries(defaults).forEach(([id, { val, suffix }]) => {
        const input = document.getElementById(id);
        const slider = document.getElementById(`${id}-slider`);
        const badge = document.getElementById(`${id}-badge`);
        if (input) input.value = val;
        if (slider) slider.value = val;
        if (badge) badge.textContent = val + suffix;
    });

    // Reset extracurricular
    const extraNo = document.getElementById('extra-no');
    if (extraNo) {
        extraNo.checked = true;
        document.querySelectorAll('.toggle-option').forEach(opt => opt.classList.remove('active'));
        const noLabel = document.getElementById('toggle-no');
        if (noLabel) noLabel.classList.add('active');
    }
}

/* ── Animate Elements on Scroll ─────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.info-card, .metric-card, .chart-card').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(24px)';
        el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        observer.observe(el);
    });
});

/* ── Auto-dismiss Flash Messages ───────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.flash').forEach(flash => {
        setTimeout(() => {
            flash.style.opacity = '0';
            flash.style.transform = 'translateY(-8px)';
            flash.style.transition = 'all 0.4s ease';
            setTimeout(() => flash.remove(), 400);
        }, 5000);
    });
});
