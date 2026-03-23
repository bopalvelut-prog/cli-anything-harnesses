import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vanguard running')
@cli.command()
def start(): click.echo('vanguard started')
if __name__ == '__main__': cli()
