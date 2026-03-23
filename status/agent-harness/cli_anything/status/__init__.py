import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('status running')
@cli.command()
def start(): click.echo('status started')
if __name__ == '__main__': cli()
