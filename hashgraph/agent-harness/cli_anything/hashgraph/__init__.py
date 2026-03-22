import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def consensus(): click.echo('Hashgraph consensus')
if __name__ == '__main__': cli()
