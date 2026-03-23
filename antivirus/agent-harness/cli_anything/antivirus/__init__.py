import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('antivirus running')
@cli.command()
def start(): click.echo('antivirus started')
if __name__ == '__main__': cli()
