// ===========================
// Dynamic CPU Options
// ===========================

const cpuBrand = document.getElementById("cpu_brand");
const cpuFamily = document.getElementById("cpu_family");
const cpuSeries = document.getElementById("cpu_series");
const gpuBrand = document.getElementById("gpu_brand");
const ramType = document.getElementById("ram_type");

function hideOptions(selectElement, values) {

    for (let option of selectElement.options) {

        option.hidden = values.includes(option.value);

    }

}

function updateOptions() {

    if (!cpuBrand) return;

    // Reset
    for (let option of cpuFamily.options) option.hidden = false;
    for (let option of cpuSeries.options) option.hidden = false;
    for (let option of ramType.options) option.hidden = false;
    for (let option of gpuBrand.options) option.hidden = false;

    const brand = cpuBrand.value;

    if (brand === "Intel") {

        hideOptions(cpuFamily, ["Ryzen", "M Series", "MediaTek", "Other"]);

        hideOptions(cpuSeries, [
            "Ryzen 3","Ryzen 5","Ryzen 7","Ryzen 9",
            "M1","M1 Pro","M1 Max",
            "M2","M2 Pro","M2 Max"
        ]);

        hideOptions(ramType, ["Unified"]);

    }

    else if (brand === "AMD") {

        hideOptions(cpuFamily, [
            "Core","Pentium","Celeron",
            "M Series","MediaTek","Other"
        ]);

        hideOptions(cpuSeries, [
            "i3","i5","i7","i9",
            "M1","M1 Pro","M1 Max",
            "M2","M2 Pro","M2 Max"
        ]);

        hideOptions(ramType, ["Unified"]);

    }

    else if (brand === "Apple") {

        hideOptions(cpuFamily, [
            "Core","Pentium","Celeron",
            "Ryzen","MediaTek","Other"
        ]);

        hideOptions(cpuSeries, [
            "i3","i5","i7","i9",
            "Ryzen 3","Ryzen 5","Ryzen 7","Ryzen 9",
            "Other"
        ]);

    }

    else if (brand === "MediaTek") {

        hideOptions(cpuFamily, [
            "Core","Pentium","Celeron",
            "Ryzen","M Series","Other"
        ]);

        hideOptions(cpuSeries, [
            "i3","i5","i7","i9",
            "Ryzen 3","Ryzen 5","Ryzen 7","Ryzen 9",
            "M1","M1 Pro","M1 Max",
            "M2","M2 Pro","M2 Max"
        ]);

        hideOptions(ramType, ["Unified"]);

    }

}

if (cpuBrand) {

    cpuBrand.addEventListener("change", updateOptions);

    updateOptions();

}

// ===========================
// Loading Button
// ===========================

const form = document.getElementById("predictionForm");
const button = document.querySelector(".predict-btn");

if (form && button) {

    form.addEventListener("submit", function () {

        button.disabled = true;
        button.innerHTML = "Predicting...";

    });

}

// ===========================
// Brand Price Chart
// ===========================

if (typeof Chart !== "undefined") {

    const canvas = document.getElementById("brandChart");

    if (canvas && typeof chartLabels !== "undefined" && typeof chartValues !== "undefined") {

        new Chart(canvas, {

            type: "bar",

            data: {

                labels: chartLabels,

                datasets: [{

                    label: "Average Price",

                    data: chartValues,

                    backgroundColor: "rgba(96,165,250,0.8)",

                    borderRadius: 10

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                plugins: {

                    legend: {

                        display: false

                    }

                },

                scales: {

                    y: {

                        beginAtZero: true,

                        ticks: {

                            color: "#ffffff"

                        },

                        grid: {

                            color: "rgba(255,255,255,0.08)"

                        }

                    },

                    x: {

                        ticks: {

                            color: "#ffffff"

                        },

                        grid: {

                            display: false

                        }

                    }

                }

            }

        });

    }

}