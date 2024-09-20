<% 
import sqlalchemy as sa
from alembic import op
%>

"""${message}"""

revision = ${up_revision!r}
down_revision = ${down_revision!r}
branch_labels = ${branch_labels!r}
depends_on = ${depends_on!r}

def upgrade():
    ${upgrades if upgrades else "pass"}

def downgrade():
    ${downgrades if downgrades else "pass"}
