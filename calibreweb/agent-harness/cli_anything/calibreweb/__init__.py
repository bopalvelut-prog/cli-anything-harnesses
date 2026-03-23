import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('calibreweb running')
@cli.command()
def start(): click.echo('calibreweb started')
if __name__ == '__main__': cli()
