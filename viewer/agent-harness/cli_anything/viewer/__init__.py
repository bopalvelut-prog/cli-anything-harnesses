import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('viewer running')
@cli.command()
def start(): click.echo('viewer started')
if __name__ == '__main__': cli()
