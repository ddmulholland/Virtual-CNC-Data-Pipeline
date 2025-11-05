const chartData = {
    temperature: [],
    spindleSpeed: [],
    feedRate: []
};

const maxDataPoints = 20;

function updateData() {
    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('machine-id').textContent = data.machine_id;
            document.getElementById('status').textContent = data.status.toUpperCase();
            document.getElementById('timestamp').textContent = new Date(data.timestamp).toLocaleTimeString();
            
            document.getElementById('temperature').textContent = data.temperature.toFixed(1);
            document.getElementById('spindle-speed').textContent = data.spindle_speed;
            document.getElementById('feed-rate').textContent = data.feed_rate;
            
            document.getElementById('pos-x').textContent = data.position.x.toFixed(3);
            document.getElementById('pos-y').textContent = data.position.y.toFixed(3);
            document.getElementById('pos-z').textContent = data.position.z.toFixed(3);
            
            document.getElementById('vibration').textContent = data.vibration.toFixed(2);
            document.getElementById('power').textContent = data.power_consumption.toFixed(2);
            
            chartData.temperature.push(data.temperature);
            chartData.spindleSpeed.push(data.spindle_speed);
            chartData.feedRate.push(data.feed_rate);
            
            if (chartData.temperature.length > maxDataPoints) {
                chartData.temperature.shift();
                chartData.spindleSpeed.shift();
                chartData.feedRate.shift();
            }
            
            drawChart('temp-chart', chartData.temperature, '#f59e0b');
            drawChart('spindle-chart', chartData.spindleSpeed, '#3b82f6');
            drawChart('feed-chart', chartData.feedRate, '#10b981');
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

function drawChart(canvasId, data, color) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width = canvas.offsetWidth;
    const height = canvas.height = canvas.offsetHeight;
    
    ctx.clearRect(0, 0, width, height);
    
    if (data.length < 2) return;
    
    const max = Math.max(...data);
    const min = Math.min(...data);
    const range = max - min || 1;
    
    const stepX = width / (maxDataPoints - 1);
    
    ctx.strokeStyle = color;
    ctx.lineWidth = 2;
    ctx.beginPath();
    
    data.forEach((value, index) => {
        const x = index * stepX;
        const y = height - ((value - min) / range) * (height - 10) - 5;
        
        if (index === 0) {
            ctx.moveTo(x, y);
        } else {
            ctx.lineTo(x, y);
        }
    });
    
    ctx.stroke();
    
    ctx.fillStyle = color + '33';
    ctx.lineTo(width, height);
    ctx.lineTo(0, height);
    ctx.closePath();
    ctx.fill();
}

updateData();
setInterval(updateData, 1000);
