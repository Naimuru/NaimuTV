//
//  ContentView.swift
//  NaimuTV
//
//  Created by Naimu on 23/03/23.
//

import SwiftUI

struct ContentView: View {
    let url: URL

    init() {
            if let clientHTMLPath = Bundle.main.path(forResource: "client", ofType: "html") {
                url = URL(fileURLWithPath: clientHTMLPath)
            } else {
                // Fallback URL if the client.html file isn't found in the app bundle
                url = URL(string: "https://example.com")!
            }
        }

    init(preview: Bool) {
        url = URL(string: "https://example.com")!
    }

    var body: some View {
        NavigationView {
            WebView(url: url)
                .navigationBarTitle("Turn Off Monitor", displayMode: .inline)
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView(preview: true)
    }
}


