# NaimuTV

<p align="center">
  <img src="https://your-logo-url.png" alt="Turn Off Monitor Logo" width="200">
</p>

NaimuTV is a simple iOS app that allows users to remotely turn off their computer monitors using their mobile devices. The app communicates with a Python server running on the target computer to send the turn-off command.

## Features

- Turn off your computer monitor remotely using your iPhone or iPad.
- Supports Windows and macOS.
- Secure communication between the iOS app and the Python server.

## Prerequisites

- Python 3.x installed on your computer
- An iOS device running iOS 13.0 or later

## Installation

1. Clone this repository:

git clone https://github.com/your-username/turn-off-monitor.git


2. Install the required Python packages:

pip install Flask flask-cors


3. Start the Python server on your computer:

cd NaimuTV
python server.py


4. Update the `ContentView.swift` file in the iOS app with the local IP address of the computer running the server script:

```swift
init() {
    url = URL(string: "http://your-computer-ip:5000/client.html")!
}
```

5. Build and run the app on your iOS device.

## Usage

1. Make sure your computer and iOS device are connected to the same local network.
2. Launch the Python server on your computer by running `python server.py` in the terminal.
3. Open the NaimuTV app on your iOS device.
4. Tap the "Turn Off Monitor" button in the app to send a command to the server running on your computer. This will turn off the computer monitor.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push your changes to the branch (`git push origin feature-branch`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.


