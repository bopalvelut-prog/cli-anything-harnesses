import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bold running')
@cli.command()
def start(): click.echo('bold started')
if __name__ == '__main__': cli()
