import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('explain running')
@cli.command()
def start(): click.echo('explain started')
if __name__ == '__main__': cli()
