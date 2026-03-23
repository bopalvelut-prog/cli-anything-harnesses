import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cantaloupe running')
@cli.command()
def start(): click.echo('cantaloupe started')
if __name__ == '__main__': cli()
