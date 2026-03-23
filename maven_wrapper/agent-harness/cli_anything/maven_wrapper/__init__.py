import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('maven_wrapper running')
@cli.command()
def start(): click.echo('maven_wrapper started')
if __name__ == '__main__': cli()
