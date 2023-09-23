describe('Prueba de búsqueda en Google', () => {
  it('Realizar búsqueda y verificar información en Wikipedia', () => {
    // Abre la página de Google
    cy.visit('https://www.google.com');
    // Busca y hace clic en el botón con el atributo id="botonAceptarTodo"
    cy.get('#W0wltc').click();
    // Utiliza JavaScript para hacer clic en el campo de búsqueda y luego escribir el texto
    cy.get('[title="Buscar"]').then(($input) => {
      $input[0].click();
      cy.wrap($input).type('automatización{enter}');
    });

    // Espera a que se cargue la página de resultados de búsqueda
    cy.url().should('include', 'search?q=automatizaci%C3%B3n');

    // Busca el link de la Wikipedia en los resultados de búsqueda
    cy.contains('Wikipedia').click();

    // Espera a que se cargue la página de Wikipedia
    // Busca y hace clic en el enlace de Wikipedia
    cy.contains('Wikipedia, la enciclopedia libre').click();

    cy.origin('https://es.wikipedia.org', () => {
      // Busca y hace scroll hasta la zona del artículo que menciona "Historia"
      cy.contains('Historia').scrollIntoView();
      // Realiza un screenshot de la página de Wikipedia
      cy.screenshot('pagina_wikipedia',{ capture: 'viewport'});
    });
    
  });
});
