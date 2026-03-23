import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jsonb running')
@cli.command()
def start(): click.echo('jsonb started')
if __name__ == '__main__': cli()
