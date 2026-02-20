document.addEventListener('DOMContentLoaded', () => {
    const semestersContainer = document.getElementById('semesters-container');
    const addSemesterBtn = document.getElementById('add-semester-btn');
    const resetBtn = document.getElementById('reset-btn');
    const exportBtn = document.getElementById('export-btn');
    
    const semTemplate = document.getElementById('semester-template');
    const subTemplate = document.getElementById('subject-template');

    const totalCgpaEl = document.getElementById('total-cgpa');
    const totalCreditsEl = document.getElementById('total-credits');
    const totalPercentageEl = document.getElementById('total-percentage');
    const finalStatusEl = document.getElementById('final-status');
    const finalBacklogsEl = document.getElementById('final-backlogs');

    let semesterCount = 0;

    // --- Main Functions ---

    function createSemester() {
        semesterCount++;
        const clone = semTemplate.content.cloneNode(true);
        const wrapper = clone.querySelector('.semester-wrapper');
        const semNum = clone.querySelector('.sem-num');
        const delBtn = clone.querySelector('.delete-sem-btn');
        const addSubBtn = clone.querySelector('.btn-add-subject');
        const subjectsList = clone.querySelector('.subjects-list');

        semNum.textContent = semesterCount;

        // Add initial 3 subjects
        for(let i=0; i<3; i++) {
            addSubject(subjectsList);
        }

        // Event Listeners
        delBtn.addEventListener('click', () => {
            wrapper.remove();
            updateAllCalculations();
            reorderSemesters();
        });

        addSubBtn.addEventListener('click', () => {
            addSubject(subjectsList);
            updateAllCalculations();
        });

        semestersContainer.appendChild(clone);
        updateAllCalculations();
    }

    function addSubject(container) {
        const clone = subTemplate.content.cloneNode(true);
        const row = clone.querySelector('.subject-row');
        const delBtn = clone.querySelector('.delete-subject-btn');
        
        // Listeners for real-time update
        row.querySelectorAll('input, select').forEach(input => {
            input.addEventListener('input', updateAllCalculations);
        });

        delBtn.addEventListener('click', () => {
            row.remove();
            updateAllCalculations();
        });

        container.appendChild(clone);
    }

    function updateAllCalculations() {
        let grandTotalPoints = 0;
        let grandTotalCredits = 0;
        let allBacklogs = [];
        let hasAnyFail = false;

        const semesterWrappers = document.querySelectorAll('.semester-wrapper');

        semesterWrappers.forEach(sem => {
            let semPoints = 0;
            let semCredits = 0;
            const rows = sem.querySelectorAll('.subject-row');
            
            rows.forEach(row => {
                const name = row.querySelector('.input-subject-name').value || "Subject";
                const credits = parseFloat(row.querySelector('.input-credits').value) || 0;
                const gradePoint = parseFloat(row.querySelector('.input-grade').value);
                
                if (!isNaN(gradePoint) && credits > 0) {
                    semPoints += (credits * gradePoint);
                    semCredits += credits;
                    
                    if (gradePoint === 0) {
                        allBacklogs.push(name);
                        hasAnyFail = true;
                    }
                }
            });

            // Update Semester-specific CGPA
            const semCgpa = semCredits > 0 ? (semPoints / semCredits) : 0;
            sem.querySelector('.sem-cgpa-val').textContent = semCgpa.toFixed(2);

            grandTotalPoints += semPoints;
            grandTotalCredits += semCredits;
        });

        // Update Overall UI
        const finalCgpa = grandTotalCredits > 0 ? (grandTotalPoints / grandTotalCredits) : 0;
        const finalPercentage = finalCgpa * 9.5;

        // Animate counter effect (basic)
        animateValue(totalCgpaEl, parseFloat(totalCgpaEl.textContent), finalCgpa, 500);
        
        totalCreditsEl.textContent = grandTotalCredits.toFixed(1);
        totalPercentageEl.textContent = finalPercentage.toFixed(2) + '%';
        
        if (hasAnyFail) {
            finalStatusEl.textContent = "FAIL";
            finalStatusEl.className = "mini-value status-fail";
            finalBacklogsEl.textContent = allBacklogs.length > 3 
                ? `${allBacklogs.slice(0,3).join(', ')}...` 
                : allBacklogs.join(', ');
        } else {
            finalStatusEl.textContent = "PASS";
            finalStatusEl.className = "mini-value status-pass";
            finalBacklogsEl.textContent = "None";
        }
    }

    function reorderSemesters() {
        const wrappers = semestersContainer.querySelectorAll('.semester-wrapper');
        semesterCount = wrappers.length;
        wrappers.forEach((w, i) => {
            w.querySelector('.sem-num').textContent = i + 1;
        });
    }

    function animateValue(obj, start, end, duration) {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            const current = progress * (end - start) + start;
            obj.innerHTML = current.toFixed(2);
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    }

    // --- Event Listeners ---

    addSemesterBtn.addEventListener('click', createSemester);

    resetBtn.addEventListener('click', () => {
        if(confirm('Are you sure you want to clear all data?')) {
            semestersContainer.innerHTML = '';
            semesterCount = 0;
            updateAllCalculations();
        }
    });

    exportBtn.addEventListener('click', () => {
        const cgpa = totalCgpaEl.textContent;
        const credits = totalCreditsEl.textContent;
        const status = finalStatusEl.textContent;
        const log = finalBacklogsEl.textContent;

        const content = `CGPA Report\n-----------\nTotal Credits: ${credits}\nFinal CGPA: ${cgpa}\nPercentage: ${totalPercentageEl.textContent}\nStatus: ${status}\nBacklogs: ${log}\n\nGenerated by Student CGPA Pro Utility.`;
        
        const blob = new Blob([content], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'cgpa_report.txt';
        a.click();
        URL.revokeObjectURL(url);
    });

    // Initial state
    createSemester();
});
