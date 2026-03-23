import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wash running')
@cli.command()
def start(): click.echo('wash started')
if __name__ == '__main__': cli()
