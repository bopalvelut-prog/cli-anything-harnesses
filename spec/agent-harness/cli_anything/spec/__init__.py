import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('spec running')
@cli.command()
def start(): click.echo('spec started')
if __name__ == '__main__': cli()
