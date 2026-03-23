import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bitrise running')
@cli.command()
def start(): click.echo('bitrise started')
if __name__ == '__main__': cli()
