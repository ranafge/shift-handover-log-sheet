import React from 'react'

const Contacts = ({contacts}) => {
    return (
        <div>
            <center><h1>Shift Handover Sheet</h1></center>
            {contacts.map((contact) => (
                <div class="card">
                    <div class="card-body">
                        <p class="card-title-shift"> {contact.shift}</p>
                        <p class="card-title">Duty Engineer:  <span className="myData">{contact.engineer_name.name}</span> </p>
                        <p class="card-title">Message: <span className="myData">  {contact.message_body}</span></p>
                        <p class="card-title">Fault Description:  <span className="myData"> {contact.Fault_description}</span></p>
                        <p class="card-title">Core Alarm:   <span className="myData"> {contact.Corealarm.alarm_name}</span></p>
                        <p class="card-title">Tx Alarm:  <span className="myData">  {contact.Transmissionalarm.alarm_name}</span></p>
                        <p class="card-title">Datacom Alarm:  <span className="myData"> {contact.Datacomalarm.alarm_name}</span></p>
                        <p class="card-title">Power Alarm:  <span className="myData"> {contact.Poweralarm.alarm_name}</span></p>
                        <p class="card-title">Action taken:   <span className="myData"> {contact.Action_taken}</span></p>
                        <p class="card-title">Date&Time:<span className="myData">  {contact.created_at}</span></p>
                        <label for="scales">SMS SEND :</label>
                         <input class="inputCheckbox" type="checkbox"  checked= {contact.have_sms_send} />
                       
                    </div>
                </div>
            ))}
        </div>
    )
};

export default Contacts