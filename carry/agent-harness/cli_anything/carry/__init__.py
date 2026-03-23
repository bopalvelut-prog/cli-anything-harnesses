import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('carry running')
@cli.command()
def start(): click.echo('carry started')
if __name__ == '__main__': cli()
