import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('hash_file')
@click.argument('wordlist')
def crack(hash_file, wordlist): subprocess.run(['hashcat', '-m', '0', hash_file, wordlist])
@cli.command()
def benchmarks(): subprocess.run(['hashcat', '-b'])
if __name__ == '__main__': cli()
