from Products.agenda import agenda


def initialize(context):
    """Inicializando"""
    context.registerClass(
        agenda.Agenda,
        constructors=(
            agenda.manage_addAgendaForm,
            agenda.manage_addAgenda,
        ),
        icon = 'imagens/calendar.png'
    )
