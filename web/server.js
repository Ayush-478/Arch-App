const url = "http://127.0.0.1:5000/chat";  // Define the correct URL
export function response(){}

export async function sendrequest(prompt) {
    try {
        const res = await fetch(url, {
            method: "POST",               // Use POST method
            headers: {
                "Content-Type": "application/json"  // Set the header to indicate JSON
            },
            body: JSON.stringify({ prompt }) // Send prompt as JSON body
        });

        if (res.ok) {
            const data = await res.json();  // Parse the JSON response
            console.log(data['res']);  // Log the response data
        } else {
            console.error("Error:", res.statusText); // Handle errors if the response isn't OK
        }
    } catch (error) {
        console.error("Request failed", error); // Catch any network or other errors
    }
}
