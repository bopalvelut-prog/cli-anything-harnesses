import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kritis running')
@cli.command()
def start(): click.echo('kritis started')
if __name__ == '__main__': cli()
