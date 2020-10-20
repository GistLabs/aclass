// type definitions for Cypress object "cy"
/// <reference types="cypress" />

describe('The Home Page', () => {

    it('can create and delete a single todo', () => {
        cy.visit('/')


        cy.contains('Add task').click()
        cy.get('#title').type('ci test todo')
        cy.get('#description').type('Have to remember to test cypress?')
        cy.contains('Save').click()

        cy.contains('ci test todo')

        cy.contains('ci test todo').first().parent().get('.delete').click()
        cy.wait(100)

    })

    it('can create and edit a single todo', () => {
        cy.visit('/')

        cy.contains('Add task').click()
        cy.get('#title').type('ci edit todo')
        cy.get('#description').type('Have to remembered to edit cypress?')
        cy.contains('Save').click()

        cy.contains('ci edit todo').first().parent().get('.edit').click()
        cy.get('#title').type('!!!!')
        cy.contains('Save').click()

        cy.contains('ci edit todo!!!!')    

        cy.contains('ci edit todo!!!!').first().parent().get('.delete').click()

        cy.wait(100)

    })
})