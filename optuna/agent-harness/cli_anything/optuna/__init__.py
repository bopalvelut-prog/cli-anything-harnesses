import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('optuna running')
@cli.command()
def start(): click.echo('optuna started')
if __name__ == '__main__': cli()
