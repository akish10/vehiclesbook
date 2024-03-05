document.getElementById('paymentForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
    
    
    var vehicleId = document.getElementById('Vehicle_id').value;

    
    var xhr = new XMLHttpRequest();
    xhr.open('POST',updateDatabaseUrl, true); 
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 200) {
            
            console.log('Database updated successfully');
            
        } else {
            
            console.error('Error updating database');
           
        }
    };
    xhr.onerror = function() {
        
        console.error('Connection error');
        
    };
    xhr.send(JSON.stringify({Vehicle_id: VehicleId}));
});
