import click
@click.group()
def cli(): pass
@cli.command()
def serve(): click.echo('SGLang serve')
@cli.command()
def benchmark(): click.echo('SGLang benchmark')
if __name__ == '__main__': cli()
