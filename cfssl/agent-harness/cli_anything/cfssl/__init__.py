import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cfssl running')
@cli.command()
def start(): click.echo('cfssl started')
if __name__ == '__main__': cli()
