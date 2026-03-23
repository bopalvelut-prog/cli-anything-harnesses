import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('requirement running')
@cli.command()
def start(): click.echo('requirement started')
if __name__ == '__main__': cli()
