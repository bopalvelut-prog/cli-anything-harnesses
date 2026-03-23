import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bubble running')
@cli.command()
def start(): click.echo('bubble started')
if __name__ == '__main__': cli()
