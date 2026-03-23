import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('think running')
@cli.command()
def start(): click.echo('think started')
if __name__ == '__main__': cli()
