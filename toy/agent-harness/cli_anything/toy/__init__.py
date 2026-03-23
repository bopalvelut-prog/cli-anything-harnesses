import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('toy running')
@cli.command()
def start(): click.echo('toy started')
if __name__ == '__main__': cli()
