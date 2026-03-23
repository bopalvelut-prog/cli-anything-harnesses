import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('school running')
@cli.command()
def start(): click.echo('school started')
if __name__ == '__main__': cli()
