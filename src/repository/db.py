from datetime import datetime

db = [
    {
      'id': 1,
      'title': 'Titulo Exemplo',
      'content': 'Conteudo Exemplo',
      'author': 'fernando',
      'createdAt': datetime(2023, 5, 17),
      'updatedAt': None,
      'comments': [
        {
          'id': 1,
          'content': 'comentário de exemplo 1',
          'author': 'fernando',
          'createdAt': datetime(2023, 5, 17),
          'updatedAt': None,
        },
        {
          'id': 2,
          'content': 'comentário de exemplo 2',
          'author': 'marcos',
          'createdAt': datetime(2023, 5, 17),
          'updatedAt': None,
        }
      ]
    },
    {
      'id': 2,
      'title': 'Titulo Exemplo 2',
      'content': 'Conteudo Exemplo 2',
      'author': 'marcos',
      'createdAt': datetime(2023, 5, 10),
      'updatedAt': None,
      'comments': [
        {
          'id': 3,
          'content': 'comentário de exemplo 3',
          'author': 'fernando',
          'createdAt': datetime(2023, 5, 17),
          'updatedAt': None,
        },
        {
          'id': 4,
          'content': 'comentário de exemplo 4',
          'author': 'marcos',
          'createdAt': datetime(2023, 5, 17),
          'updatedAt': None,
        }
      ]
    }
  ]
