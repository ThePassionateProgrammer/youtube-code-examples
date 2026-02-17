


Decorator (All Participate)        Chain of Responsibility (Choose Path)

Client                             Client
  |                                  |
  v                                  v
[Required] --> [Email] --> [Base]   [Required] --> [Email]
    |            |                    |           |
    v            v                    |           |
  always runs   always runs           |           |
                                     decide here ─┘