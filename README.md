<h1>anniversaires</h1>
Un programme qui gère les anniversaires.

Grâce à ce programme, n'oubliez plus ni les prochains anniversaires, ni la météo.  
[<img width=200 alt="capture de l'écran d'accueil"
src="https://github.com/sev1527/anniversaires/blob/main/metadata/capture_accueil.jpg?raw=true">](https://github.com/sev1527/anniversaires/blob/main/metadata/capture_accueil.jpg?raw=true)

<h2>Fonctionnalités</h2>
<h3>Un éditeur dans l'application</h3>
<p>Cliquez sur le bouton "voir les données" pour l'ouvrir.</p>
<a href="https://github.com/sev1527/anniversaires/blob/main/metadata/capture_modifier.jpg"><img src="https://github.com/sev1527/anniversaires/blob/main/metadata/capture_modifier.jpg" alt="capture de l'écran de modifications"></a>
<h3>La météo à portée de main</h3>
<p>Cliquez sur le bouton "météo" et observez la météo des cinq prochains jours. Météo par <a href="https://prevision-meteo.ch/">prevision-meteo.ch</a>.</p>
<a href="https://github.com/sev1527/anniversaires/blob/main/metadata/capture_météo.jpg"><img src="https://github.com/sev1527/anniversaires/blob/main/metadata/capture_météo.jpg" alt="capture de l'écran d'affichage de la météo"></a>

<h2>Prérequis</h2>
<ul>
  <li>python 3 (<a href="https://www.python.org/" target="_blank">site officiel</a>)</li>
  <li>Pillow (utilisez <code>python3 -m pip install Pillow</code> pour installer <a href="https://pillow.readthedocs.io/en/stable/installation.html" rel="help" target="_blank">plus</a>)</li>
  <li>requests (utilisez <code>python3 -m pip install requests</code> pour installer <a href="https://pypi.org/project/requests/" rel="help" target="_blank">plus</a>)</li>
  <li>numpy (utilisez <code>python3 -m pip install numpy</code> pour installer <a href="https://pypi.org/project/numpy/" rel="help" target="_blank">plus</a>)</li>
  <li>PyQt5 (utilisez <code>python3 -m pip install PyQt5</code> pour installer <a href="https://pypi.org/project/PyQt5/" rel="help" target="_blank">plus</a>)</li>
</ul>

<h2>Questions/réponses</h2>
<h3>Ce programme collecte-t-il mes informations personnelles ?</h3>
<p><strong>Non</strong></p>
<h3>Je souhaite changer la ville de la météo. Comment faire ?</h3>
<p>Ouvrez le programme en mode édition et changez la ville ligne 27.</p>
<h3>Le programme m'affiche des fausses fêtes. Que faire ?</h3>
<p>Signalez-le moi dans <a href="https://github.com/sev1527/anniversaires/issues">l'onglet issues</a>. Comme pour tout autre problème.</p>
<h3>J'aimerais que le programme se lance au démarrage de l'ordinateur.</h3>
<p>Tutoriel pour Windows :</p>
<ol>
  <li>Exécutez le raccourcis clavier <kbd>win</kbd>+<kbd>R</kbd>.</li>
  <li>Tapez <code>taskschd.msc</code> puis <kbd>entrée</kbd>.</li>
  <li>Dans la barre de droite, faites un clic droit sur "Bibliothèque du planificateur de tâches". Puis nouveau dossier et donnez-lui le nom de votre choix. <a href="https://github.com/sev1527/anniversaires/blob/main/metadata/capture_tâche_nouveau_dossier.jpg"><img src="https://github.com/sev1527/anniversaires/blob/main/metadata/capture_tâche_nouveau_dossier.jpg" alt="capture d'écran"></a></li>
  <li>Ouvrez le dossier puis faites un clic droit dans la zone blanche, puis "Créer une nouvelle tâche de base". <a href="https://github.com/sev1527/anniversaires/blob/main/metadata/capture_tâche_nouvelle_tâche.jpg"><img src="https://github.com/sev1527/anniversaires/blob/main/metadata/capture_tâche_nouvelle_tâche.jpg" alt="capture d'écran"></a></li>
  <li>Nommez-la et décrivez-la comme bon vous semble puis cliquez sur suivant.</li>
  <li>Choisissez "Quand j'ouvre une session" puis cliquez sur suivant.</li>
  <li>Choisissez "Démarrer un programme" puis cliquez sur suivant.</li>
  <li>Entrez dans la case "Programme/script" le chemin d'accès du fichier "pythonw.exe", situé dans le même dossier que l'interpréteur python, entre guillemets suivis du chemin d'accès au script du programme ("C:\users\...\anniversaire.py") puis cliquez sur suivant.</li>
  <li>Cliquez sur terminer.</li>
  <li>Sélectionnez la tâche puis cliquez sur "exécuter" dans le menu de droite pour la tester.</li>
</ol>
<p>En cas de problème pendant ces étapes, signalez le dans <a href="https://github.com/sev1527/anniversaires/issues">l'onglet issues</a>.</p>
