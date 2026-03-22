import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def namespaces(): click.echo('Temporal namespaces')
@cli.command()
def workflows(): click.echo('Running workflows')
if __name__ == '__main__': cli()
