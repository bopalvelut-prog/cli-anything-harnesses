import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('victory running')
@cli.command()
def start(): click.echo('victory started')
if __name__ == '__main__': cli()
