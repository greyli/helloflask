@app.cli.command('init')
@click.option('--drop-table', is_flag=True, help='Re-create the tables.')
def init_command(drop_table):
    """Initialize the application."""
    if drop_table:
        query = text("DROP TABLE IF EXISTS :table_name")
        db.engine.execute(query, table_name='users')
        click.echo('Dropped tables.')
    db.create_all()
    click.echo('Initialized.')