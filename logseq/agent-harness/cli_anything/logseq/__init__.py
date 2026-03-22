import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def graph(): click.echo('Logseq graph')
@cli.command()
def pages(): click.echo('Logseq pages')
if __name__ == '__main__': cli()
