import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shellcheck running')
@cli.command()
def start(): click.echo('shellcheck started')
if __name__ == '__main__': cli()
