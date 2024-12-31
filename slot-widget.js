const SlotWidget = (function () {
    let config = {};
  
    // Initialize the widget
    function init(options) {
      config = options;
      const container = document.getElementById(config.containerId);
      if (!container) {
        console.error("Container not found!");
        return;
      }
  
      // Render the UI
      renderUI(container);
    }
  
    // Render the widget UI
    function renderUI(container) {
      container.innerHTML = `
        <h3>Book a Slot</h3>
        <form  id="slot-form">
        <div class="slot-input">
        <input type="text" required placeholder='name' id="user-name">
        <input type = "number" required placeholder='phone' id = "user-phone">
      <input type="date" id="date-input" required />
            </div>
          <ul id="slot-list"></ul>
          <button type="submit">Book Selected Slot</button>
        </form>
        <div id="response-message"></div>
      `;
  
      const dateInput = document.getElementById('date-input');
      dateInput.addEventListener('change', handleDateChange);
  
      const form = document.getElementById('slot-form');
      form.addEventListener('submit', handleFormSubmit);
    }
  
    // Fetch available slots for a specific date
    async function handleDateChange(event) {
      const date = event.target.value;
      const slotList = document.getElementById('slot-list');
      slotList.innerHTML = '<li>Loading slots...</li>';
  
      try {
        const response = await fetch(`${config.apiUrl}?date=${date}`);
        const slots = await response.json();
        console.log(slots);
        
        if (slots.length === 0) {
          slotList.innerHTML = '<li>No slots available for this date.</li>';
          return;
        }
  
        // Display available slots
        slotList.innerHTML = '';
        slots.forEach(slot => {
          const li = document.createElement('li');
          li.innerHTML = `
          <input type="radio" name="slot" value="${slot.id}" id="slot-${slot.id}" />
          <label for="slot">${slot.slot}</label>
          `;
          slotList.appendChild(li);
        });
      } catch (e) {
        slotList.innerHTML = `<li>Error fetching slots</li>`;
      }
    }
  
    // Handle form submission
    async function handleFormSubmit(event) {
      event.preventDefault();
  
      const date = document.getElementById('date-input').value;
      const name = document.getElementById('user-name').value;
      const phone = document.getElementById('user-phone').value;
      const selectedSlot = document.querySelector('input[name="slot"]:checked');
  
      if (!selectedSlot) {
        document.getElementById('response-message').innerHTML = '<p>Please select a slot to book.</p>';
        return;
      }
  
      try {
        const response = await fetch(config.bookingUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            date: date,
            time_slot_id: selectedSlot.value,
            name: name, 
            phone:phone
          }),
        });
  
        const result = await response.json();
        document.getElementById('response-message').innerHTML = `<p>Booking successful! ID: ${result.id}</p>`;
      } catch (e) {
        
        document.getElementById('response-message').innerHTML = `<p>Error: Slot may be already booked</p>`;
      }
    }
  
    // Public API
    return { init };
  })();
  
  