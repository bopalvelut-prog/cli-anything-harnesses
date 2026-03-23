import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('adguard running')
@cli.command()
def start(): click.echo('adguard started')
if __name__ == '__main__': cli()
