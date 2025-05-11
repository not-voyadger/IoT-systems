document.addEventListener("DOMContentLoaded", () => {
  const ctx = document.getElementById("temperatureChart").getContext("2d");
  let chart;

  function renderChart(data) {
    const labels = data.map(item => item.timestamp);
    const temps = data.map(item => item.temperature);

    if (chart) chart.destroy();

    chart = new Chart(ctx, {
      type: "line",
      data: {
        labels: labels,
        datasets: [{
          label: "Temperature (°C)",
          data: temps,
          borderColor: "rgba(75,192,192,1)",
          fill: false,
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
      }
    });
  }

  function updateTable(data) {
    const tbody = document.querySelector("#dataTable tbody");
    tbody.innerHTML = "";
    data.forEach(item => {
      const row = document.createElement("tr");
      row.innerHTML = `<td>${item.timestamp}</td><td>${item.temperature}</td>`;
      tbody.appendChild(row);
    });
  }

  async function fetchData() {
    const res = await fetch("/api/data");
    const data = await res.json();
    renderChart(data);
    updateTable(data);
  }

  document.getElementById("deleteBtn").addEventListener("click", async () => {
    await fetch("/api/delete", { method: "DELETE" });
    fetchData();
  });

  fetchData();
});
