CREATE TABLE skin_lesion (
    id INT PRIMARY KEY AUTO_INCREMENT,
    code VARCHAR(10) NOT NULL,
    name VARCHAR(50) NOT NULL,
    description TEXT 
);

ALTER TABLE skin_lesion ADD CONSTRAINT UQ_skin_lesion_code UNIQUE(code);

ALTER TABLE skin_lesion RENAME COLUMN name to latin_name;

ALTER TABLE skin_lesion ADD polish_name varchar(50) AFTER latin_name;

INSERT INTO skin_lesion (id, code, latin_name, polish_name, description) VALUES (
	null,
	'bcc',
	'Basal cell carcinoma',
	'Rak podstawnokomórkowy skóry',
	'Rak podstawnokomórkowy skóry najczęściej objawia się jako mała, perłowa grudka lub płaska, bliznowata zmiana na skórze, która może mieć nacieczoną powierzchnię. Zmiany te często występują na obszarach ciała narażonych na słońce, takich jak twarz, szyja i ręce.<br/><b>Inne objawy:</b><br/>Zmiana może rosnąć powoli, stając się większa i bardziej widoczna. Może również krwawić, tworzyć strupy lub nie goić się przez dłuższy czas.<br/><b>Niebezpieczeństwo związane z chorobą:</b><br/>Rak podstawnokomórkowy jest najczęstszym typem raka skóry, który rzadko daje przerzuty, ale może być destrukcyjny miejscowo. Nieleczony, może prowadzić do uszkodzenia sąsiadujących tkanek, w tym kości.<br/><br/>W przypadku zaobserwowania podejrzanych zmian skórnych, które nie goją się lub zmieniają wygląd, należy skonsultować się z dermatologiem.'
);

INSERT INTO skin_lesion (id, code, latin_name, polish_name, description) VALUES (
	null,
	'scc',
	'Carcinoma cutaneum squamosum',
	'Rak kolczystokomórkowy skóry',
	'Rak kolczystokomórkowy skóry często pojawia się jako czerwone, łuszczące się plamy, guzki z owrzodzeniem, które mogą rosnąć i krwawić. Zmiany te mogą występować na skórze narażonej na działanie słońca, takie jak twarz, uszy, szyja, wargi i grzbiety rąk.<br/><b>Inne objawy:</b><br/>Zmiana może być bolesna, swędząca i może rosnąć szybciej niż rak podstawnokomórkowy. W zaawansowanych stadiach może wystąpić przerzut do innych części ciała.<br/><b>Niebezpieczeństwo związane z chorobą:</b><br/>Rak kolczystokomórkowy jest bardziej agresywny niż rak podstawnokomórkowy i może prowadzić do przerzutów, jeśli nie jest leczony. Wczesne wykrycie i leczenie są kluczowe dla zapobieżenia poważnym komplikacjom.<br/><br/>Jeśli zauważysz jakiekolwiek podejrzane zmiany na skórze, które rosną, krwawią lub nie goją się, należy natychmiast skonsultować się z dermatologiem.'
);

INSERT INTO skin_lesion (id, code, latin_name, polish_name, description) VALUES (
	null,
	'mel',
	'Melanoma malignum',
	'Czerniak',
	'Czerniak to złośliwy nowotwór skóry, który często wygląda jak nowe znamię lub zmiana w istniejącym znamieniu. Zmiany mogą mieć nieregularne krawędzie, różne kolory (czarny, brązowy, czerwony, biały, niebieski), asymetryczny kształt i średnicę większą niż 6 mm.<br/><b>Inne objawy:</b><br/>Czerniak może swędzieć, krwawić lub tworzyć owrzodzenia. W późniejszych stadiach mogą pojawić się przerzuty do innych części ciała, powodując ból, obrzęki i inne objawy ogólnoustrojowe.<b>Niebezpieczeństwo związane z chorobą:</b><br/>Czerniak jest jednym z najbardziej agresywnych nowotworów skóry, który może szybko rozprzestrzeniać się na inne części ciała, co znacznie utrudnia leczenie. Wczesne wykrycie i leczenie są kluczowe dla poprawy rokowań.<br/><br/>W przypadku zaobserwowania jakichkolwiek podejrzanych zmian skórnych należy niezwłocznie skonsultować się z dermatologiem lub onkologiem.'
);