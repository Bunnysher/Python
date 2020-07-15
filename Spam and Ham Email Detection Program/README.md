# Reversi in Java


**Objective**:  
This program filters emails and determines if they are malicious (spam) or safe (ham) by implementing the Naive Bayes Classifier.

**Structure of the code**:  
Στον κώδικα που υλοποιήθηκε σε Python, ουσιαστικά, κρατώντας την συχνότητα των λέξεων που βρίσκονται σε ham και spam email των training datasets, καθορίζουμε έαν ένα νέο email πρέπει να καταταχθεί στην spam είτε στην ham κατηγορία βάσει των λέξεων που περιλαμβάνει. Για βελτίωση των αποτελεσμάτων και καλύτερο classification των νέων text messages χρησιμοποίησαμε την μέθοδο διόρθωσης του Laplace προσθέτοντας στην πιθανότητα εμφάνισης κάθε λέξης ενός μηνύματος τον αριθμό ένα. Ακόμα δίνεται η επιλογή στον χρήστη να παράγει αποτελέσματα με δυο μεθόδους: α) με τον αλγόριθμο στην μορφή που βρίσκεται χωρίς καμία περαιτέρω διόρθωση και β) με χρήση της αντίστροφης ποσότητα της συχνότητας των λέξεων (Inverse Document Frequency - IDF). Με την χρήση της IDF, ουσιαστικά λέξεις που εμφανίζονται πολύ συχνά στα emails όπως για παράδειγμα ειδικοί χαρακτήρες (τελεία, κόμμα, “Subject” κτλπ.) αποδυναμώνονται και η αξία τους στο classification ενός νέου text message ως ham ή spam μειώνεται. Συνεπώς, όσο αυξάνεται η συνχότητα εμφάνισης μιας λέξης, μειώνεται η αξία της στην κατηγοριοποίηση του νέου email. 
Training  και Testing
Χρησιμοποιήσαμε τα data των “Ling-Spam” για να κάνουμε train και testing στον αλγόριθμό μας. Παρακάτω ως False Negative (FN) αναφέρονται spam emails που έγιναν classify λανθασμένα ως ham, ως  True Negative (TN) αναφέρονται ham emails που έγιναν classify σωστά ως ham, ως False Positive (FP) αναφέρονται ham emails που έγιναν classify λανθασμένα ως spam και ως True Positive (TP) αναφέρονται spam emails που έγιναν classify σωστά ως spam.
