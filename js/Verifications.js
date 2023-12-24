function VerifMax(nom) 
{
	var max = 3;
	var compteur = 0;
	var checkboxes = document.getElementsByName(nom);
	for (var i = 0; i < checkboxes.length; i++) 
	{
		if (checkboxes.item(i).checked == true) 
		{
			compteur++
			if (compteur > max) 
			{
				checkboxes.item(i).checked = false;
				alert("3 réponses possibles maximum");
			}
		}
	}
}