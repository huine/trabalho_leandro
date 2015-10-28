from Products.agenda import agenda


def initialize(context):
    """Inicializando"""
    context.registerClass(
        agenda.Agenda,
        constructors=(
            agenda.manage_addAgendaForm,
            agenda.manage_add_agenda,
        ),
        icon = 'imagens/icon2.png'
    )
