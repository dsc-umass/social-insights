const functions = require('firebase-functions');
const admin = require('firebase-admin');

admin.initializeApp(functions.config().firebase);

let db = admin.firestore();

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
// exports.helloWorld = functions.https.onRequest((request, response) => {
//  response.send("Hello from Firebase!");
// });

exports.myFunctionName = functions.firestore
    .document('trending-searches/searches-log').onUpdate((change, context) => {
        
        let newValue = change.after.data();

        let searchesLog = db.collection('trending-searches').doc('searches-log');
        let getJSON = searchesLog.get()
        .then(doc => {
            if (!doc.exists) {
            console.log('No such document!');
            return "error"
            } else {
            console.log('Document data:', doc.data());
            return doc.data()
            }
        })
        .catch(err => {
            console.log('Error getting document', err);
        });



    });
